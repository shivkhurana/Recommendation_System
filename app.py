from flask import Flask, jsonify, request
import time
from functools import lru_cache

app = Flask(__name__)

# Mock Data Store
products = [{"id": i, "category": "tech"} for i in range(1000)]

# OPTIMIZATION: In-Memory Caching for speed
@lru_cache(maxsize=1000)
def get_recommendations_logic(user_id):
    # Simulate ML compute time (Content Filtering)
    time.sleep(0.02) 
    return products[:5]

@app.route('/recommend', methods=['POST'])
def recommend():
    start_time = time.time()
    user_id = request.json.get('user_id')
    
    # Fetch results
    recs = get_recommendations_logic(user_id)
    
    # Calculate latency for monitoring
    latency_ms = (time.time() - start_time) * 1000
    
    return jsonify({
        "user_id": user_id,
        "recommendations": recs,
        "latency_ms": f"{latency_ms:.2f}ms" # Visible metric for debugging
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)