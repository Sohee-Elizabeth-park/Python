import pandas as pd

def generate_create_table_sql(csv_file, table_name):
    # CSV 파일 읽기
    df = pd.read_csv(csv_file)
    
    # 컬럼 정보 추출 및 SQL 문 생성
    columns = []
    primary_keys = []
    comments = []
    
    for _, row in df.iterrows():
        column_def = f"{row['column_name']} {row['data_type']}"
        
        # Not Null 조건 추가
        if row['not_null'] == 'Not Null':
            column_def += " NOT NULL"
        
        # 기본값이 있으면 추가
        if not pd.isna(row['default']):
            column_def += f" DEFAULT {row['default']}"
        
        columns.append(column_def)
        
        # 키가 있으면 추가 (예: PRIMARY KEY)
        if row['key'] == 'PK':
            primary_keys.append(row['column_name'])
        
        # 주석이 있으면 추가
        if not pd.isna(row['comment']):
            comments.append(f"COMMENT ON COLUMN {table_name}.{row['column_name']} IS '{row['comment']}';")
    
    # CREATE TABLE SQL 문 생성
    create_table_sql = f"CREATE TABLE {table_name} (\n    " + ",\n    ".join(columns)
    
    if primary_keys:
        create_table_sql += f",\n    CONSTRAINT pk_{table_name} PRIMARY KEY (" + ", ".join(primary_keys) + ")"
    
    create_table_sql += "\n);"
    
    # 주석을 추가하는 SQL 문 추가
    if comments:
        create_table_sql += "\n" + "\n".join(comments)
    
    return create_table_sql

# CSV 파일 경로와 테이블 이름 지정
csv_file = r'(CSV 파일 경로)'
table_name = '(테이블명)'

# SQL 생성 및 출력
create_table_sql = generate_create_table_sql(csv_file, table_name)
print(create_table_sql)
