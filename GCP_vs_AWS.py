'''
Este é um script a fim de patricar sobre a criação de arquivos em CSV usando Python!

Como exemplo para o conteúdo do nosso arquivo CSV, usarei informações sobre as principais ferramentas do GCP, 
comparadas com as ferramentas da AWS.

Quais ferramentas cada Cloud tem?
Quais as diferenças e semelhanças?
Qual ferramenta X é equivalente para executar a mesma demanda entre uma Cloud e outra?
'''

import pandas as pd

# Criando os dados da comparação
data = {
    "Categoria": [
        "Armazenamento de Dados", "Armazenamento de Dados", "Armazenamento de Dados", "Armazenamento de Dados", "Armazenamento de Dados",
        "Processamento de Dados", "Processamento de Dados", "Processamento de Dados", "Processamento de Dados", "Processamento de Dados",
        "Análise e Visualização de Dados", "Análise e Visualização de Dados", "Análise e Visualização de Dados",
        "Mensageria e Streaming", "Mensageria e Streaming"
    ],
    "GCP": [
        "Cloud Storage", "BigQuery", "Cloud SQL", "Cloud Spanner", "Firestore",
        "Dataflow", "Dataproc", "Cloud Composer", "Cloud Functions", "Cloud Run",
        "Looker / Looker Studio", "BigQuery ML", "Vertex AI",
        "Pub/Sub", "Dataflow (Streaming)"
    ],
    "AWS": [
        "S3 (Simple Storage Service)", "Amazon Redshift", "Amazon RDS", "Amazon Aurora / DynamoDB", "Amazon DynamoDB",
        "AWS Glue / Kinesis Data Analytics", "Amazon EMR (Elastic MapReduce)", "Amazon MWAA (Managed Workflows for Apache Airflow)",
        "AWS Lambda", "AWS Fargate",
        "Amazon QuickSight", "Redshift ML", "Amazon SageMaker",
        "Amazon SNS + SQS", "Amazon Kinesis"
    ]
}

# Criando um DataFrame
df = pd.DataFrame(data)

# Salvando como CSV
file_path = "/mnt/data/gcp_vs_aws_tools.csv"
df.to_csv(file_path, index=False, encoding="utf-8")

file_path
