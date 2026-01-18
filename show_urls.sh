#!/bin/bash
echo "🌐 روابط الدخول المباشرة:"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Get Codespace name
CODESPACE_NAME="${CODESPACE_NAME:-unknown}"
GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN="${GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN:-githubpreview.dev}"

echo ""
echo "🎨 الواجهة الرئيسية (Streamlit):"
echo "   https://${CODESPACE_NAME}-8501.${GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}"
echo ""
echo "🔌 الـ API (FastAPI):"
echo "   https://${CODESPACE_NAME}-8000.${GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}"
echo ""
echo "📚 التوثيق التفاعلي:"
echo "   https://${CODESPACE_NAME}-8000.${GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}/docs"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "💡 أو ببساطة:"
echo "   VS Code → PORTS (أسفل) → اضغط 🌐 بجانب المنفذ"
echo ""
