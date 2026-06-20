from boxes.models import Box


class BoxSelector:

    @staticmethod
    def recommend(order):

        total_weight = 0
        total_volume = 0

        max_length = 0
        max_width = 0
        max_height = 0

        for item in order.items.all():

            product = item.product
            quantity = item.quantity

            total_weight += product.weight * quantity

            product_volume = (
                product.length
                * product.width
                * product.height
            )

            total_volume += product_volume * quantity

            max_length = max(max_length, product.length)
            max_width = max(max_width, product.width)
            max_height = max(max_height, product.height)

        valid_boxes = []

        for box in Box.objects.all():

            if total_weight > box.max_weight:
                continue

            if total_volume > box.volume:
                continue

            if max_length > box.length:
                continue

            if max_width > box.width:
                continue

            if max_height > box.height:
                continue

            valid_boxes.append(box)

        if not valid_boxes:
            return None

        valid_boxes.sort(key=lambda b: b.cost)

        return valid_boxes[0]
    