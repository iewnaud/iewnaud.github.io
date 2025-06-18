from scholarly import scholarly, ProxyGenerator
import json
from datetime import datetime
import os

# ✅ 启用代理绕过封锁，注意传入 repeat 参数
pg = ProxyGenerator()
pg.FreeProxies(repeat=2)
scholarly.use_proxy(pg)

# 🔍 Scholar 抓取逻辑
author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']: v for v in author['publications']}

# 📝 保存结果
os.makedirs('results', exist_ok=True)
with open('results/gs_data.json', 'w') as f:
    json.dump(author, f, ensure_ascii=False)

shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": f"{author['citedby']}",
}
with open('results/gs_data_shieldsio.json', 'w') as f:
    json.dump(shieldio_data, f, ensure_ascii=False)
