# Oddělení a přetypování správných labelů
true, c, mapping_mask = tf.split(y_true, [1, 1, 1], axis=-1)
c_int = tf.cast(tf.squeeze(c, axis=-1), dtype=tf.int32)
mapping_mask = tf.cast(mapping_mask, dtype=tf.bool)

# Vytvoření one-hot enkódované masky pro relevantní kanály
num_channels = y_pred.shape[-1]
channel_mask = tf.one_hot(c_int, depth=num_channels, axis=-1)

# Použití one-hot enkódované masky pro výběr relevantních kanálů
y_pred_selected = tf.reduce_sum(y_pred * channel_mask, axis=-1, keepdims=True)

# Výpočet kvadratické chyby
mse_loss = tf.square(y_pred_selected - true)

# Použití výpočetní masky pro zarhnutí pouze relevantních oblastí snímku
masked_loss = tf.where(mapping_mask, mse_loss, tf.zeros_like(mse_loss))

# Finální výpočet kvadratické chyby normalizované o počet pozitivních hodnot masky
loss = (tf.reduce_sum(masked_loss) / 
        tf.reduce_sum(tf.cast(mapping_mask, tf.float32)))