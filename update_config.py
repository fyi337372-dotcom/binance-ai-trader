import json

# Read current config
with open('C:/Users/Administrator/.openclaw/openclaw.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# Add plugin config
config['plugins']['load'] = {
    "paths": ["C:\\Users\\Administrator\\.openclaw\\workspace\\plugins\\memory-lancedb-pro"]
}
config['plugins']['slots'] = {
    "memory": "memory-lancedb-pro"
}
config['plugins']['entries']['memory-lancedb-pro'] = {
    "enabled": True,
    "config": {
        "embedding": {
            "apiKey": "${JINA_API_KEY}",
            "model": "jina-embeddings-v5-text-small",
            "baseURL": "https://api.jina.ai/v1",
            "dimensions": 1024,
            "normalized": True
        },
        "autoCapture": True,
        "autoRecall": False,
        "retrieval": {
            "mode": "hybrid",
            "vectorWeight": 0.7,
            "bm25Weight": 0.3,
            "minScore": 0.45,
            "hardMinScore": 0.55,
            "rerank": "cross-encoder",
            "rerankProvider": "jina",
            "rerankApiKey": "${JINA_API_KEY}",
            "rerankModel": "jina-reranker-v3",
            "candidatePoolSize": 20
        }
    }
}

# Write updated config
with open('C:/Users/Administrator/.openclaw/openclaw.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, indent=2, ensure_ascii=False)

print("Done!")
