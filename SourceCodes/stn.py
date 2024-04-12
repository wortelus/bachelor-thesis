# Výstup lokalizační sítě
local_inputs = self.localization_net(inputs)
# Výstup regresních parametrů theta
theta = self.regressor_net(local_inputs)

# Tvorba vzorkového pole
grid = transformed_grid(self.height, self.width, theta)
# X a Y vzorkového pole
xS = grid[:, 0, :, :]
yS = grid[:, 1, :, :]

# Transformace vstupu STN pomocí bilineární interpolace
outputs = bilinear_sampler(inputs, xS, yS)

# První výstup tvoří transformovaný obraz
# Druhý výstup tvoří pomocný výstup do ztrátové funkce
return [outputs, theta]