def ppm_to_mg_per_day(ppm, daily_dose_g):
    return (ppm * daily_dose_g) / 1000

def pde_compliance(ppm, daily_dose_g, pde_limit_mg):
    intake = ppm_to_mg_per_day(ppm, daily_dose_g)
    return intake <= pde_limit_mg, intake
