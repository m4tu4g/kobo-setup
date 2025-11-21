import json
import requests
import sys


NOTION_TOKEN = 'ntn_xxx'

NOTION_PAGES_API_URL = "https://api.notion.com/v1/pages"
NOTION_BLOCKS_API_URL = "https://api.notion.com/v1/blocks"
NOTION_API_HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2025-09-03"
}


def create_notion_page(title, parent_page_id):
    create_page_payload = {
        "parent": {
            "type": "page_id",
            "page_id": parent_page_id
        },
        "properties": {
            "title": [
                {
                    "type": "text",
                    "text": {
                        "content": title
                    }
                }
            ]
        }
    }

    response = requests.post(NOTION_PAGES_API_URL, headers=NOTION_API_HEADERS, json=create_page_payload)

    if response.status_code == 200:
        return response.json()['id']
    else:
        print(f"Error creating page: {response.status_code}, {response.text}")
        return None


def add_text_to_page(page_id, text):
    add_block_url = NOTION_BLOCKS_API_URL + f"/{page_id}/children"
    
    blocks_payload = {
        "children": [
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": text
                            }
                        }
                    ]
                }
            }
        ]
    }

    response = requests.patch(add_block_url, headers=NOTION_API_HEADERS, json=blocks_payload)

    if response.status_code != 200:
        print(f"Error adding text block: {response.status_code}, {response.text}")
    else:
        print(f"added text block to page {page_id}")


def create_chapters_from_entries(entries, root_page_id):
    chapters = {}

    for entry in entries:
        chapter = entry['chapter']
        text = '"' + entry['text'] + '"'
        if 'note' in entry:
            text += "\n" + entry['note']  # append note to text if it exists
        
        if chapter not in chapters:
            chapters[chapter] = []

        chapters[chapter].append(text + "\n")

    for chapter_title, chapter_texts in chapters.items():
        print(f"Creating page for {chapter_title}")
        chapter_page_id = create_notion_page(chapter_title, root_page_id)
        
        if chapter_page_id:
            for text in chapter_texts:
                add_text_to_page(chapter_page_id, text)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: notion_sync.py <page_id> <json_path>")
        sys.exit(1)

    page_id = sys.argv[1]
    json_path = sys.argv[2]
    with open(json_path, "r") as f:
        json_data = json.load(f)
    
    create_chapters_from_entries(json_data['entries'], page_id)
