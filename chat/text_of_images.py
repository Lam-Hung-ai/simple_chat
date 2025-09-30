import base64
from langchain_google_genai import ChatGoogleGenerativeAI

def get_text_from_image(image_path: str):
    
    with open(image_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode("utf-8")
    key = "AIzaSyAvxhnEnALX3hxxiOC9q0VLNwYAOrpOk2k"
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key=key)

    message = {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Trong ảnh về thông tin bưu kiện, hãy đọc toàn bộ văn bản trong ảnh",
            },
            {
                "type": "image",
                "source_type": "base64",
                "data": image_data,
                "mime_type": "image/jpeg",
            },
        ],
    }
    response = llm.invoke([message])
    return response.content

def get_text_from_images(images_path: list[str]) -> list[str]:
    texts = []
    for image_path in images_path:
        image_data = get_text_from_image(image_path)
        texts.append(image_data)
    return texts


if __name__ == "__main__":
    texts = get_text_from_images(["../images/0.jpeg", "../images/1.jpeg"])
    for text in texts:
        print(text)