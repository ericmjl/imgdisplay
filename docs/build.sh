# Create website
pandoc index.md \
    -o index.html \
    -c template/notes.css \
    -H template/header.html \
    --template template/template.html

git add .
git commit
git push
