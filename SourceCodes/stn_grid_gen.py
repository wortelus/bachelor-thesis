# Vytvoření polí pro normalizovaný souřadnicový systém
x = tf.linspace(-1.0, 1.0, width)
y = tf.linspace(-1.0, 1.0, height)
(x, y) = tf.meshgrid(x, y)

# Převedení do 1D
x = tf.reshape(x, [-1])
y = tf.reshape(y, [-1])

# Změna tvaru do [[xs], [ys] , [1]] (v homogenní formě)
sampling_grid = tf.stack([x, y, tf.ones_like(x)])  # (3, H*W)

# Rozšíření skalárního pole do velikosti dávky (ang. batch)
sampling_grid = tf.broadcast_to(sampling_grid, (batch, 3, height * width))

# Transformace vzorkovacího pole pomocí afinní transformačních parametrů
sampling_grid = tf.matmul(theta, sampling_grid)

# Změna tvaru vzorkovacího pole do (dávka, 2, výška, šířka)
sampling_grid = tf.reshape(sampling_grid, [batch, 2, height, width])