import pandas as pd
import os

def generate_create_table_sql(csv_file, foreign_keys_info):
    # CSV 파일 읽기, 인코딩을 cp949로 지정
    df = pd.read_csv(csv_file, encoding='cp949')
    
    # 파일명에서 확장자를 제거하여 테이블 이름 추출
    table_name = os.path.splitext(os.path.basename(csv_file))[0]
    
    # 컬럼 정보 추출 및 SQL 문 생성
    columns = []
    primary_keys = []
    foreign_keys = []
    comments = []
    
    for _, row in df.iterrows():
        # 공백을 밑줄(_)로 대체한 컬럼 이름 생성
        column_name = row['column_name'].replace(" ", "_")
        
        column_def = f"{column_name} {row['data_type']}"
        
        # Not Null 조건 추가
        if row['not_null'] == 'Not Null':
            column_def += " NOT NULL"
        
        # 기본값이 있으면 추가
        if not pd.isna(row['default']):
            column_def += f" DEFAULT {row['default']}"
        
        columns.append(column_def)
        
        # 키가 있으면 추가 (예: PRIMARY KEY)
        if row['key'] == 'PK':
            primary_keys.append(column_name)
        
        # 외래 키가 있으면 추가
        if row['key'] == 'FK':
            foreign_table = foreign_keys_info.get(column_name)
            if foreign_table:
                foreign_keys.append(f"FOREIGN KEY ({column_name}) REFERENCES {foreign_table}({column_name})")
        
        # 주석이 있으면 추가
        if not pd.isna(row['comment']):
            comments.append(f"COMMENT ON COLUMN {table_name}.{column_name} IS '{row['comment']}';")
    
    # CREATE TABLE SQL 문 생성
    create_table_sql = f"CREATE TABLE {table_name} (\n    " + ",\n    ".join(columns)
    
    if primary_keys:
        create_table_sql += f",\n    CONSTRAINT pk_{table_name} PRIMARY KEY (" + ", ".join(primary_keys) + ")"
    
    if foreign_keys:
        create_table_sql += f",\n    " + ",\n    ".join(foreign_keys)
    
    create_table_sql += "\n);"
    
    # 주석을 추가하는 SQL 문 추가
    if comments:
        create_table_sql += "\n" + "\n".join(comments)
    
    return create_table_sql

# CSV 파일 경로 지정
csv_file = r'C:\Users\sohee\Documents\Personal\csv\파일이름.csv'

# 외래 키 정보 지정
foreign_keys_info = {
    'column_name1': 'reference_table1',
    'column_name2': 'reference_table2',
    # Add more column to table mappings as needed
}

# SQL 생성 및 출력
create_table_sql = generate_create_table_sql(csv_file, foreign_keys_info)
print(create_table_sql)
