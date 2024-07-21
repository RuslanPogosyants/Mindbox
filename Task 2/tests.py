import unittest
from pyspark.sql import SparkSession

from main import get_product_category_pairs


class TestProductCategoryPairs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spark = SparkSession.builder.appName("TestProductCategory").getOrCreate()

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    def test_product_category_pairs(self):
        products_data = [(1, "Product A"), (2, "Product B"), (3, "Product C")]
        categories_data = [(1, "Category 1"), (2, "Category 2")]
        product_category_data = [(1, 1), (1, 2), (2, 1)]

        products_df = self.spark.createDataFrame(products_data, ["product_id", "product_name"])
        categories_df = self.spark.createDataFrame(categories_data, ["category_id", "category_name"])
        product_category_df = self.spark.createDataFrame(product_category_data, ["product_id", "category_id"])

        pairs, no_category_products = get_product_category_pairs(products_df, categories_df, product_category_df)

        # Проверяем, что пары продуктов и категорий правильные
        expected_pairs = [("Product A", "Category 1"), ("Product A", "Category 2"), ("Product B", "Category 1")]
        actual_pairs = [(row.product_name, row.category_name) for row in pairs.collect()]

        self.assertCountEqual(actual_pairs, expected_pairs)

        # Проверяем, что продукты без категорий правильные
        expected_no_category_products = ["Product C"]
        actual_no_category_products = [row.product_name for row in no_category_products.collect()]

        self.assertCountEqual(actual_no_category_products, expected_no_category_products)


if __name__ == '__main__':
    unittest.main()
