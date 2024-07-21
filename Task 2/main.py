from pyspark.sql import SparkSession
from pyspark.sql import functions as F


def get_product_category_pairs(products_df, categories_df, product_category_df):
    # Объединяем датафреймы продуктов и категорий по их связям
    product_category_pairs = products_df.join(
        product_category_df,
        on='product_id',
        how='left'
    ).join(
        categories_df,
        on='category_id',
        how='left'
    ).select(
        'product_name',
        'category_name'
    )

    # Получаем продукты без категорий
    products_without_categories = products_df.join(
        product_category_df,
        on='product_id',
        how='left_anti'
    ).select('product_name')

    return product_category_pairs, products_without_categories

