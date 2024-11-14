class Solution:
    def minimizedMaximum(self, n, quantities):
        """
            You are given an integer n indicating there are n specialty retail stores. There are m product types of varying amounts, which are given as a 0-indexed integer array quantities, where quantities[i] represents the number of products of the ith product type.

            You need to distribute all products to the retail stores following these rules:
            
            A store can only be given at most one product type but can be given any amount of it.
            After distribution, each store will have been given some number of products (possibly 0). Let x represent the maximum number of products given to any store. You want x to be as small as possible, i.e., you want to minimize the maximum number of products that are given to any store.
            Return the minimum possible x.
        """
        m = len(quantities)

        type_store_pairs = [(-q, q, 1) for q in quantities]

        heapq.heapify(type_store_pairs)

        for _ in range(n - m):
            (
                neg_ratio,
                total_quantity_of_type,
                stores_assigned_to_type,
            ) = heapq.heappop(type_store_pairs)

            new_stores_assigned_to_type = stores_assigned_to_type + 1
            new_ratio = total_quantity_of_type / new_stores_assigned_to_type

            heapq.heappush(
                type_store_pairs,
                (
                    -new_ratio,
                    total_quantity_of_type,
                    new_stores_assigned_to_type,
                ),
            )

        _, total_quantity_of_type, stores_assigned_to_type = heapq.heappop(
            type_store_pairs
        )

        return math.ceil(total_quantity_of_type / stores_assigned_to_type)
