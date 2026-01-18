#!/bin/bash
echo "🚀 تشغيل Streamlit في Codespaces..."
echo ""
poetry run streamlit run src/sa/ui/app.py \
  --server.port 8501 \
  --server.address 0.0.0.0 \
  --server.headless true \
  --browser.serverAddress localhost \
  --browser.gatherUsageStats false
