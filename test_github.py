from app.github.client import get_pr_files


files = get_pr_files(
    "pulkit8888",
    "ai-code-review-test",
    1
)


for file in files:

    print(
        file["filename"]
    )

    print(
        file["patch"]
    )
