import numpy as np
#Data Generation
np.random.seed(42)
n = 500

height_cm = np.round(np.random.normal(170, 9, n), 1)
weight_kg = np.round(0.9 * (height_cm - 100) + np.random.normal(0, 8, n) + 8, 1)
gender = np.random.randint(0, 2, n)

height_cm[[10, 77, 301]] = 0
weight_kg[[45, 200]] = -1 

print(height_cm[:5])
print(weight_kg[:5])
print(gender[:5])

print(height_cm.shape)
print(height_cm.min(), height_cm.max())
print(weight_kg.min(), weight_kg.max())

#cleaning
valid = (height_cm > 0) & (weight_kg > 0)
print("Valid rows:", valid.sum())
print("Invalid rows:", (~valid).sum())

h = height_cm[valid]
w = weight_kg[valid]
g = gender[valid]

print(f"Height: mean={np.mean(h):.2f}, median={np.median(h):.1f}, std={np.std(h):.2f}")
print(f"Weight: mean={np.mean(w):.2f}, median={np.median(w):.1f}, std={np.std(w):.2f}")

bmi = np.round(w / (h / 100) ** 2, 2)
print(bmi[:5])
print(bmi.min(), bmi.max(), round(bmi.mean(), 2))
underweight = (bmi < 18.5).sum()
normal = ((bmi >= 18.5) & (bmi < 25)).sum()
overweight = ((bmi >= 25) & (bmi < 30)).sum()
obese = (bmi >= 30).sum()
total = len(bmi)
for label, count in [("Underweight", underweight), ("Normal", normal),
("Overweight", overweight), ("Obese", obese)]:
    
  print(f"{label:10}: {count:3} ({count / total * 100:.1f}%)")

corr = np.corrcoef(h, w)[0, 1]
print(f"Correlation: {corr:.3f}")

group0 = (g == 0)
group1 = (g == 1)
print("Group 0:", group0.sum(), "members")
print("Group 1:", group1.sum(), "members")
print(f"Avg height: {h[group0].mean():.2f} vs {h[group1].mean():.2f}")
print(f"Avg weight: {w[group0].mean():.2f} vs {w[group1].mean():.2f}")
print(f"Avg BMI: {bmi[group0].mean():.2f} vs {bmi[group1].mean():.2f}")

z = (h - h.mean()) / h.std()
outliers = h[np.abs(z) > 2.5]
print("Height outliers:", len(outliers), outliers)
print("BMI quartiles:", np.percentile(bmi, [25, 50, 75]))