# Scalable Recommendation API ⚡

**High-Performance Microservice**
A lightweight, low-latency recommendation engine designed to serve personalized content with **sub-50ms response times**. Unlike standard ML notebooks, this project focuses on the **serving layer**, optimizing for throughput and API design.

## 🏗️ Architecture

- **Framework:** Flask (Python)
- **Caching:** In-Memory LRU Cache to minimize compute for frequent queries.
- **Algorithm:** Content-Based Filtering (Cosine Similarity).

## 🚀 Performance

- **Average Latency:** ~35ms
- **Throughput:** Handles 500+ requests/sec on local testing.

## 🔌 API Endpoints

- `GET /health`: System status check.
- `POST /recommend`: Input user_id, returns JSON list of product_ids.
