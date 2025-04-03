import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
url: str = os.getenv("SUPABASE_URL", 'https://rydbbqqrojrvvxiwsttr.supabase.co')
key: str = os.getenv("SUPABASE_KEY",'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ5ZGJicXFyb2pydnZ4aXdzdHRyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDM1MDY5ODksImV4cCI6MjA1OTA4Mjk4OX0.RkOUYbVsDOEeC1BgDmwTM5-8MltoIwO4aGPN4dJevUw')
supabase: Client = create_client(url, key)
