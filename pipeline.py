from prefect import flow

from dim_pelanggan_etl import etl_dim_pelanggan_flow
from dim_produk_etl import etl_dim_produk_flow
from dim_toko_etl import flow_etl_dim_toko
from dim_kurir_etl import etl_dim_kurir_flow
from dim_waktu_etl import flow_etl_dim_waktu
from fact_sales_etl import etl_fact_sales_flow
from fact_delivery_etl import etl_fact_delivery_flow
from fact_target_sales_etl import etl_fact_target_sales_flow

@flow(name="Pipeline ETL Sederhana", description="Contoh flow untuk materi kuliah SI")
def etl_flow():
    etl_dim_pelanggan_flow()
    etl_dim_produk_flow()
    flow_etl_dim_toko()
    etl_dim_kurir_flow()
    flow_etl_dim_waktu()
    etl_fact_sales_flow()
    etl_fact_delivery_flow()
    etl_fact_target_sales_flow()

if __name__ == "__main__":
    etl_flow()