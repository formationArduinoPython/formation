# approximations de la tangente à l'origine
tau_inconnue_ms = 12
plt.plot([0, tau_inconnue_ms, tau_inconnue_ms],[0, ChargeMax, 0],
         linewidth=0.8, linestyle="--", color = "cyan",
         label = "tangente à l'origine, ordonnée maximale à t = {} ms".format(tau_inconnue_ms))
