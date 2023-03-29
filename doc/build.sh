pandoc "./report.md" "./metadata.yaml" \
    --output="./report.pdf" \
    --from markdown \
    --template="./eisvogel.tex" \
    --resource-path="./" \
    --listings \
    --number-sections -V colorlinks=true -V linkcolor=blue -V urlcolor=blue -V toccolor=gray \
    --pdf-engine=xelatex
