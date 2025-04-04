'''
Este é um script a fim de patricar sobre a criação de arquivos em CSV usando Python!

Como exemplo para o conteúdo do nosso arquivo CSV, usarei informações sobre as principais ferramentas do GCP, 
comparadas com as ferramentas da AWS.

Quais ferramentas cada Cloud tem?
Quais as diferenças e semelhanças?
Qual ferramenta X é equivalente para executar a mesma demanda entre uma Cloud e outra?
'''

import pandas as pd

# Dados da comparação entre as 2 Clouds
data = {
    "Categoria": [
        "Object Storage", "Data Warehouse", "Banco Relacional Gerenciado", "Banco Relacional Escalável", "Banco NoSQL",
        "ETL / ELT", "Processamento em Lote / Big Data", "Orquestração de Workflows", "Funções Serverless", "Contêineres Serverless",
        "BI / Dashboards", "Machine Learning no DW", "Plataforma de IA/ML Gerenciada",
        "Mensageria Assíncrona", "Processamento de Streaming"
    ],
    "GCP": [
        "Cloud Storage", "BigQuery", "Cloud SQL", "Cloud Spanner", "Firestore",
        "Dataflow", "Dataproc", "Cloud Composer", "Cloud Functions", "Cloud Run",
        "Looker / Looker Studio", "BigQuery ML", "Vertex AI",
        "Pub/Sub", "Dataflow (Streaming)"
    ],
    "AWS": [
        "Amazon S3", "Amazon Redshift", "Amazon RDS", "Amazon Aurora", "Amazon DynamoDB",
        "AWS Glue", "Amazon EMR", "Amazon MWAA", "AWS Lambda", "AWS Fargate",
        "Amazon QuickSight", "Redshift ML", "Amazon SageMaker",
        "Amazon SNS + SQS", "Amazon Kinesis"
    ]
}

# Agora vamos criar o dataframe
df = pd.DataFrame(data)

# Salvando como Excel formatado
output_path = "gcp_vs_aws_tools_formatted.xlsx"
with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    df.to_excel(writer, index=False, sheet_name='Comparativo GCP vs AWS')

print(f"Arquivo Excel salvo em: {output_path}")



