# IMDb Sentiment Analysis Deployment

## Render

1. Push project to GitHub
2. Create Render account
3. New Web Service
4. Connect GitHub repository
5. Select repository
6. Build Command:

pip install -r requirements.txt

7. Start Command:

uvicorn src.api.app:app --host 0.0.0.0 --port $PORT

8. Deploy

API will be available at:

https://your-app-name.onrender.com/docs