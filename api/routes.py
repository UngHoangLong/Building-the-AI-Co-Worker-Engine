from fastapi import APIRouter, Request

router = APIRouter()


@router.post("/message")
async def handle_message(request: Request):
    data = await request.json()
    # TODO: Nhận message từ user, gửi vào queue, trả về kết quả từ agent
    # Ví dụ response mẫu:
    example_response = {
        "ai_response": "Tôi không chắc cô hiểu rõ mô hình của Gucci Group. Chúng ta có 9 thương hiệu độc lập...",
        "state": {
            "trust_score": 40,
            "tension_score": 30,
            "patience_level": 95
        }
    }
    return {"status": "received", "data": data, "result": example_response}
