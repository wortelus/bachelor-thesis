# Přídavný řádek pro vytvoření homogenní transformační matice
homogeneous_row = tf.constant([[[0., 0., 1.]]])
# Vyplnění řádku do rozměrů velikosti dávky
theta_homogeneous_tiled = tf.tile(homogeneous_row, [tf.shape(theta)[0], 1, 1])
# Tvorba homogenní transformační matice
theta_homogeneous = tf.concat([theta, theta_homogeneous_tiled], axis=1)

# Výpočet inverzní transformační matice, jelikož
# vzorkovník modulu STN funguje na inverzních hodnotách
theta_homogeneous_inv = tf.linalg.inv(theta_homogeneous)

# Homogenní transformace
transformed_coords = tf.matmul(coords_homogeneous_reshaped, 
                               theta_homogeneous_inv, 
                               transpose_b=True)