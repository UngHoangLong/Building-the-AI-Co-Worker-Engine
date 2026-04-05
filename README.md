# AI Job Simulation Engine

## Kiến trúc tổng quan
- Multi-Agent System: Support Agent, Main Agent, Director Local Agent, Director Global Agent
- 3-Layer Cognitive Architecture: Core Ontology, Semantic Reflex, Dynamic State
- Data: Persona JSON, Redis (state), Pinecone/Milvus (vector db)
- Event-driven Microservices, Pub/Sub, SSE/WebSocket

## Cấu trúc thư mục
- agents/: Các agent chính
- data/: Quản lý dữ liệu, state, RAG
- orchestration/: Điều phối, queue, event
- api/: API layer
- tools/: MCP client, tích hợp tool nội bộ
- utils/: Tiện ích chung

## Cài đặt
```bash
pip install -r requirements.txt
```

## Khởi tạo nhanh
- Chạy thử FastAPI: `uvicorn api.main:app --reload`

## Ghi chú
- Mỗi agent là một worker độc lập, giao tiếp qua Redis queue/pubsub.
- State lưu ở Redis, knowledge lưu ở vector db.
- Tích hợp tool qua MCP.
