#!/bin/bash

echo "🛑 Stopping All SA Platform Services..."
echo "════════════════════════════════════════════════════════════════════"

# Kill all services
pkill -f "streamlit" && echo "✅ Stopped Streamlit services"
pkill -f "uvicorn" && echo "✅ Stopped FastAPI services"
pkill -f "jupyter" && echo "✅ Stopped Jupyter"
pkill -f "mlflow" && echo "✅ Stopped MLflow"
pkill -f "python -m http.server" && echo "✅ Stopped HTTP servers"

echo ""
echo "🧹 Cleanup complete!"
echo "════════════════════════════════════════════════════════════════════"
