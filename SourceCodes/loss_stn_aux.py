overshoots = (tf.maximum(norm_transformed_x - NORMALIZED_MAX, 0) +
              tf.maximum(NORMALIZED_MIN - norm_transformed_x, 0) +
              tf.maximum(norm_transformed_y - NORMALIZED_MAX, 0) +
              tf.maximum(NORMALIZED_MIN - norm_transformed_y, 0))