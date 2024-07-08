CreateSqlOra
=============
##### CSV 파일 내 컬럼 정보로 테이블 생성 SQL문 자동화 코드 작성
- - -
< 파일 수정 내역 >
|파일명|업로드 일자|수정내역|
|---|---|---|
|CreateSqlOra_1.1v.py|2024-07-08-월|UnicodeDecode 에러 해결|
|CreateSqlOra_1.0v.py|2024-07-08-월|최초 업로드|
- - -

||설명|
|---|---|
|**작성일**|2024-07-08-목|
|**개발 목적**|테이블 정의서(.xlsx)를 바탕으로 Oracle DB에 테이블 생성 필요로 인한 테이블 생성 쿼리 작성이 번거로운 문제 해결 위함|
|**Skills**|Python 3.12.4, Pandas, Oracle 12 Client, Oracle Server 11g|
|**Tool용**|VSC, DBeaver|
|**Code Name**|CreateSqlOra.py|
- - -
##### <로직>
1. CSV 파일에 형식을 맞춰 컬럼 정보 기입
2. VSC에서 Python 코드 실행
3. 출력 된 SQL 코드 복사
4. DBeaver 내 SQL Script에 복사한 SQL 코드 붙여넣고 실행
- - -
##### <CSV 파일>
다음의 형식을 맞춰 컬럼 정보 기입
(* 기재 된 row data는 예시)
|column_name|NO|data_type|type_mod|not_null|key|default|comment|
|---|---|---|---|---|---|---|---|
|A|1|VARCHAR(1)||Not Null|FK|'Y'|판매단가|
|B|2|NUMBER||Not Null|PK|1000||
|C|3|
* ###### not_null : null 허용할 수 없는 경우, Not Null로 기입
* ###### key : foreign key인 경우 FK, primary key인 경우 PK
* ###### default : 문자열이면 ‘(문자열)’
