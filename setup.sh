echo "Setting up FastAPI project on Ubuntu..."

sudo apt update

sudo apt install -y python3 python3-pip python3-venv

python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip

if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Installing packages manually..."
    pip install fastapi uvicorn sqlalchemy pydantic bcrypt python-multipart jinja2 python-dotenv
fi

echo ""
echo "✅ Installation complete!"
echo ""
echo "To run the application:"
echo "1. Activate virtual environment: source venv/bin/activate"
echo "2. Run: uvicorn app.main:app --reload"
echo "3. Open: http://localhost:8000"