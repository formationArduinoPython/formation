# approximations de la tangente à l'origine
tau_inconnue_us = 12000
plt.plot([0, tau_inconnue_us, tau_inconnue_us],[0, ChargeMax, 0],
         linewidth=0.8, linestyle="--", color = "cyan",
         label = "tangente à l'origine, ordonnée maximale à t = {} $\\mu$s".format(tau_inconnue_us))
