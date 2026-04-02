from ingestion.pipeline import run_pipeline

if __name__ == "__main__":
    run_pipeline("data/data1.pdf")
    run_pipeline("data/data2.docx")