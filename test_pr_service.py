from app.services.pr_service import PRService

files = PRService.get_changed_files(
    owner="pulkit8888",
    repository="ai-code-review-test",
    pr_number=1,
)

print("=" * 60)

for file in files:
    print(file)

print("=" * 60)