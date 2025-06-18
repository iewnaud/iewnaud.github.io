from scholarly import scholarly
import json
from datetime import datetime
import os

author = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']: v for v in author['publications']}

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
