C:\Users\bhata\Pythonprojects\locust>python -m venv .venvloc
C:\Users\bhata\Pythonprojects\locust>cd .venvloc
C:\Users\bhata\Pythonprojects\locust\.venvloc>cd Scripts
C:\Users\bhata\Pythonprojects\locust\.venvloc\Scripts>activate
(.venvloc) C:\Users\bhata\Pythonprojects\locust\.venvloc\Scripts>cd ../../

(.venvloc) C:\Users\bhata\Pythonprojects\locust>pip install -r requirements.txt



Create Class extending HttpUser
Create tasks
locust -f locust.py --host http://localhost:8080 --users 2 --spawn-rate 10

git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/nagarajsv3/locust-poc.git
git push -u origin main