To implement the Freedom Dividend plan, the following modeling steps were performed:
1. **Project a baseline policy** to 2019 using Tax-Calculator. While Yang has said his plan wouldn't go into effect until 2021, using 2019 allows people to envision their current income and enter it in the Plan Explorer.
2. **Project a reform policy** to 2019 using Tax-Calculator, which eliminates the payroll tax cap and treats capital gains as normal income (other parts of the reform are implemented outside Tax-Calculator). This is specified as the following Tax-Calculator reform:
`{'SS_Earnings_c': {2019: 1e+16}, 'CG_nodiff': {2019: True}}`
3. **Calculate the difference in combined tax liability** between the baseline and reform.
4. **Extract income and relevant benefits** from the TaxData CPS file. Relevant benefits include Social Security, Unemployment Insurance, SSI, TANF, SNAP, and WIC.
5. **Duplicate each tax unit** in the file, to split citizens and noncitizens. The weight for the citizen tax units was multiplied by 0.93, while the weight for noncitizens was multiplied by 0.07, in accord with the Kaiser Family Foundation's [estimates](https://www.kff.org/other/state-indicator/distribution-by-citizenship-status/). A future revision will include actual citizenship status from the CPS; the TaxData file omits it.
6. **Determine each tax unit's maximum UBI** by multiplying the number of adult citizens by $1,000 per month.
    *Note: I do not treat the UBI as taxable income, given the Yang campaign's funding models did not include taxability, and the challenges of recipients comparing their current untaxed benefits to a taxable UBI when making choices.*
7. **Simultaneously calculate each tax unit's Freedom Dividend and new benefit amounts,** depending on the benefit amount and maximum UBI:
    1. Tax units whose maximum UBI exceeds the total benefit amount (across all 6 benefit categories) accept the full UBI and decline their existing benefits (if they have any);
    2. Tax units whose current benefits exceed their maximum UBI amount decline the UBI
8. **Calculate the Tax Policy Center's definition of Expanded Cash Income (ECI),** including the new UBI and adjusted benefits. Not all components are available, so this is an approximation used to match their estimated incidence by ECI quantile.
9. **Calculate each tax unit's ECI percentile rank.** In accord with TPC, these are weighted such that each decile has an equal number of people. Tax units are ordered by unadjusted ECI, rather than ECI divided by the square-root of the number of people in the tax unit, as TPC does.
10. **Simulate the Value Added Tax,** which Yang defines at 10% totaling $800 billion per year, in two stages:
    1. Multiply each tax unit's after-tax income (ECI minus taxes) by their respective row in the "Broad base" column of this chart from a TPC [report](https://www.taxpolicycenter.org/briefing-book/who-would-bear-burden-vat), based on their ECI percentile rank.
    ![TPC VAT distribution table](https://imgur.com/SITCD7r.png)
    2. Scale each tax unit's VAT amount by a constant to ensure the total VAT is $800 billion, as Yang has indicated (Yang proposes a 10% VAT, vs. the 5% policy modeled by TPC). The scaling factor in this case was 1.65.
11. **Simulate the Financial Transaction Tax,** which Yang defines as 0.1% totaling $50 billion per year, in a similar way:
    1. Multiply each tax unit's after-tax income (ECI minus taxes, not subtracting the VAT) by their respective column height in this chart from a Tax Policy Center [report](https://www.taxpolicycenter.org/sites/default/files/alfresco/publication-pdfs/2000587-financial-transaction-taxes.pdf), based on their ECI percentile rank.
    2. Scale each tax unit's FTT amount by a constant to ensure the total FTT is $50 billion, as Yang has indicated (Yang proposes a 0.1% FTT, while the TPC paper doesn't show the rate modeled in their chart). The scaling factor in this case was 1.42.
    ![TPC FTT distribution chart](https://imgur.com/KdtuCKr.png)
12. **Simulate the carbon tax,** which Yang defines as $40 per metric ton. Since Yang proposes that half of the carbon tax fund clean energy projects, only include the $20 per metric ton that would go toward the Freedom Dividend. Multiply each tax unit's after-tax income (excluding the VAT or FTT) by the corresponding rate in the final column of the below chart from the Treasury Department's 2017 [report](https://www.treasury.gov/resource-center/tax-policy/tax-analysis/Documents/WP-115.pdf), and scale down by $20 / $49 (the fee modeled by Treasury) = 0.41. Yang has not estimated a total amount, so we use the resultant $83 billion total.
![Treasury carbon tax distributional impact table](https://imgur.com/mODSEYq.png)


The income-based approach for estimating the tax incidence does not account for heterogeneity within income group. This omission results in less spread of the net effect of the Freedom Dividend than is shown. For example, tax units with more people may incur greater VAT incidence than estimated here, and tax units with fewer people may incur a smaller VAT incidence.
