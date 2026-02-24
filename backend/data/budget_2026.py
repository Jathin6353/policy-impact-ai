"""
Union Budget 2026-27 - Comprehensive Policy Data
Presented: 1 February 2026 by Finance Minister Nirmala Sitharaman

Source: https://www.indiabudget.gov.in
"""

# ============================================
# MACROECONOMIC OVERVIEW
# ============================================
MACRO_OVERVIEW = {
    "fiscal_year": "2026-27",
    "presentation_date": "2026-02-01",
    "total_expenditure_cr": 5347000,  # ₹53.47 lakh crore
    "total_revenue_cr": 3650000,      # ₹36.5 lakh crore
    "capital_expenditure_cr": 1220000, # ₹12.2 lakh crore
    "fiscal_deficit_percent_gdp": 4.3,
    "debt_to_gdp_percent": 55.6,
    "nominal_gdp_growth_percent": 10.0,
    "revenue_deficit_percent_gdp": 1.5,
    "primary_deficit_percent_gdp": 0.8,
}

# ============================================
# INFRASTRUCTURE & CONNECTIVITY
# ============================================
INFRASTRUCTURE_POLICIES = {
    "capex_allocation_cr": 1220000,  # ₹12.2 lakh crore
    
    "high_speed_rail_corridors": {
        "count": 7,
        "description": "Seven new high-speed rail corridors for inter-city mobility",
        "estimated_investment_cr": 150000,
    },
    
    "national_waterways": {
        "count": 20,
        "description": "20 National Waterways to be operationalised for inland transport",
        "estimated_investment_cr": 25000,
    },
    
    "freight_corridor": {
        "route": "Dankuni to Surat",
        "description": "Dedicated freight corridor to streamline logistics",
        "estimated_investment_cr": 50000,
    },
    
    "city_economic_regions": {
        "investment_per_cer_cr": 5000,
        "duration_years": 5,
        "description": "Integrated investment zones for Tier-2 & Tier-3 cities",
        "total_investment_cr": 25000,
    },
    
    "seaplane_viability_gap_funding": {
        "description": "Support for indigenous seaplane manufacturing & operations",
        "allocation_cr": 2000,
    },
}

# ============================================
# MANUFACTURING & INDUSTRY
# ============================================
MANUFACTURING_POLICIES = {
    "semiconductor_mission_2": {
        "name": "India Semiconductor Mission 2.0",
        "allocation_cr": 76000,
        "description": "Enhanced funding for world-class semiconductor ecosystem & IP creation",
        "targets": ["Fab units", "ATMP facilities", "Design ecosystem", "R&D centres"],
    },
    
    "ecms": {
        "name": "Electronics Component Manufacturing Scheme",
        "allocation_cr": 40000,
        "description": "Support for domestic electronics component manufacturing",
        "sectors": ["PCBs", "Passive components", "Sensors", "Displays"],
    },
    
    "container_manufacturing_fund": {
        "name": "Container Manufacturing Fund",
        "allocation_cr": 10000,
        "description": "Domestic container ecosystem development",
        "target_capacity": "500,000 TEUs/year by 2030",
    },
    
    "chemical_parks_scheme": {
        "name": "Chemical Parks Scheme",
        "description": "Support for states to build plug-and-play infrastructure",
        "allocation_cr": 8000,
    },
    
    "rare_earth_corridors": {
        "name": "Rare Earth Corridors",
        "states": ["Odisha", "Andhra Pradesh", "Kerala", "Tamil Nadu"],
        "description": "Critical minerals & supply chain security",
        "allocation_cr": 15000,
    },
    
    "biopharma_shakti": {
        "name": "Biopharma SHAKTI",
        "allocation_cr": 10000,
        "description": "Upgraded institutes, clinical trial centres for biopharma",
        "components": ["Research institutes", "Clinical trials", "Manufacturing", "Export hubs"],
    },
}

# ============================================
# MSME & ENTREPRENEURSHIP
# ============================================
MSME_POLICIES = {
    "sme_growth_fund": {
        "name": "SME Growth Fund",
        "allocation_cr": 10000,
        "description": "Scale MSMEs into global champions",
        "target_beneficiaries": 50000,
    },
    
    "self_reliant_india_fund": {
        "name": "Self-Reliant India Fund (Additional)",
        "additional_allocation_cr": 2000,
        "description": "For micro enterprises",
        "total_corpus_cr": 22000,
    },
    
    "treds_mandate": {
        "name": "TReDS Mandatory for PSUs",
        "description": "Central PSUs must use TReDS platform for MSME payments",
        "expected_benefit_cr": 25000,
        "payment_cycle_reduction_days": 15,
    },
    
    "corporate_mitras": {
        "name": "Corporate Mitras",
        "description": "Professional compliance groups to assist MSMEs",
        "target_msmes": 100000,
    },
}

# ============================================
# AGRICULTURE & RURAL DEVELOPMENT
# ============================================
AGRICULTURE_POLICIES = {
    "bharat_vistaar": {
        "name": "Bharat-VISTAAR",
        "description": "AI-powered advisory tool integrated with AgriStack",
        "features": [
            "Real-time crop recommendations",
            "Weather-based alerts",
            "Market price information",
            "Pest & disease advisory",
            "Input optimization"
        ],
        "allocation_cr": 5000,
        "target_farmers_cr": 10,  # 10 crore farmers
    },
    
    "fisheries_modernization": {
        "name": "Fisheries Value Chain Modernization",
        "allocation_cr": 2761,
        "components": ["Cold chain", "Processing", "Export infrastructure"],
    },
    
    "high_value_crops": {
        "name": "High-Value Plantation Support",
        "crops": ["Sandalwood", "Walnuts", "Cashew", "Cocoa"],
        "target": "Global Brand Status by 2030",
        "allocation_cr": 3000,
    },
    
    "veterinary_training": {
        "name": "Veterinary Professional Training",
        "target_professionals": 20000,
        "loan_subsidy_percent": 50,
        "allocation_cr": 1000,
    },
    
    "khadi_village_industry": {
        "name": "Mahatma Gandhi Gram Swaraj",
        "description": "Khadi & Village industry revitalisation",
        "allocation_cr": 2500,
    },
}

# ============================================
# EMPLOYMENT & SKILLS
# ============================================
EMPLOYMENT_POLICIES = {
    "employment_linked_incentives": {
        "name": "Employment-Linked Incentives",
        "description": "Incentives for first-time employees",
        "allocation_cr": 15000,
        "target_jobs_lakh": 50,
    },
    
    "skill_loan_scheme": {
        "name": "Revised Skill Loan Scheme",
        "max_loan_amount": 750000,  # Up to ₹7.5 lakh
        "interest_subsidy_percent": 3,
        "allocation_cr": 5000,
    },
    
    "research_fellowships": {
        "name": "Research Fellowships",
        "positions": 10000,
        "institutions": ["IITs", "IISc", "NITs", "Central Universities"],
        "monthly_stipend": 75000,
        "allocation_cr": 9000,
    },
}

# ============================================
# HEALTH & SOCIAL WELFARE
# ============================================
HEALTH_POLICIES = {
    "health_allocation_cr": 95000,
    "family_welfare_cr": 35000,
    
    "ayushman_bharat_expansion": {
        "name": "Ayushman Bharat Expansion",
        "coverage_increase_cr": 5,  # 5 crore more families
        "new_coverage_limit": 700000,  # Increased to ₹7 lakh
    },
    
    "maternal_child_health": {
        "name": "Maternal & Child Health Mission",
        "allocation_cr": 12000,
        "target": "Zero preventable maternal deaths by 2030",
    },
}

# ============================================
# ENERGY & ENVIRONMENT
# ============================================
ENERGY_POLICIES = {
    "rooftop_solar": {
        "name": "PM Surya Ghar Muft Bijli Yojana",
        "additional_allocation_cr": 5000,
        "target_households_cr": 1,  # 1 crore households
        "subsidy_percent": 40,
    },
    
    "bioenergy": {
        "name": "Bioenergy Mission",
        "allocation_cr": 3000,
        "focus": ["Biogas", "Biofuel", "Biomass power"],
    },
    
    "battery_manufacturing": {
        "name": "Battery Manufacturing Support",
        "allocation_cr": 8000,
        "target_capacity_gwh": 50,
    },
    
    "solar_glass": {
        "name": "Solar Glass Manufacturing",
        "allocation_cr": 2000,
        "description": "Reduce import dependency for solar panels",
    },
    
    "green_hydrogen": {
        "name": "Green Hydrogen Mission",
        "allocation_cr": 19700,
        "production_target_mt": 5,  # 5 Million Tonnes by 2030
    },
}

# ============================================
# TRANSPORT & TOURISM
# ============================================
TRANSPORT_TOURISM = {
    "udan_expansion": {
        "name": "UDAN Enhanced Support",
        "allocation_cr": 4500,
        "new_routes": 100,
        "regional_airports": 50,
    },
    
    "coastal_waterways": {
        "name": "Coastal & Inland Waterways Expansion",
        "allocation_cr": 6000,
        "new_terminals": 25,
    },
    
    "destination_digital_grid": {
        "name": "National Destination Digital Knowledge Grid",
        "description": "Digital documentation of tourist destinations",
        "allocation_cr": 1500,
        "destinations_covered": 500,
    },
    
    "adventure_tourism": {
        "name": "Adventure Tourism Trails",
        "allocation_cr": 1000,
        "trails": 50,
        "states": ["Uttarakhand", "Himachal", "Sikkim", "Ladakh", "Northeast"],
    },
}

# ============================================
# DEFENCE & SECURITY
# ============================================
DEFENCE_POLICIES = {
    "total_defence_allocation_cr": 682000,  # ₹6.82 lakh crore
    "capital_outlay_cr": 172000,
    "revenue_expenditure_cr": 510000,
    
    "intelligence_bureau_capex_cr": 6782,
    
    "indigenization_target_percent": 75,
    "domestic_procurement_cr": 128000,
}

# ============================================
# FEDERAL & STATE FINANCE
# ============================================
FEDERAL_FINANCE = {
    "finance_commission": "16th Finance Commission",
    "states_share_percent": 41,  # 41% of central taxes
    "panchayat_grants_cr": 791000,  # ₹7.91 lakh crore
    
    "special_assistance": {
        "backward_regions_cr": 15000,
        "northeast_states_cr": 8000,
        "himalayan_states_cr": 5000,
    },
}

# ============================================
# DIGITAL & AI INITIATIVES
# ============================================
DIGITAL_POLICIES = {
    "ai_mission": {
        "name": "India AI Mission",
        "allocation_cr": 10372,
        "components": ["Compute infrastructure", "AI startups", "Skill development"],
    },
    
    "data_localisation": {
        "name": "Data Localisation Support",
        "tax_holiday_till": 2047,
        "description": "Tax holiday for foreign cloud/digital operators using Indian data centres",
    },
    
    "digital_infrastructure": {
        "name": "Digital Public Infrastructure",
        "allocation_cr": 5000,
        "projects": ["UPI expansion", "DigiLocker", "ONDC", "Account Aggregator"],
    },
}

# ============================================
# EASE OF DOING BUSINESS
# ============================================
EASE_OF_BUSINESS = {
    "new_income_tax_act": {
        "name": "Income Tax Act, 2025",
        "replaces": "Income Tax Act, 1961",
        "effective_from": "2026-04-01",
        "key_changes": [
            "Simplified language",
            "Reduced sections",
            "Digital-first compliance",
            "Faceless assessments default",
        ],
    },
    
    "revised_return_deadline": {
        "old_deadline": "December 31",
        "new_deadline": "March 31",
        "description": "Extended deadline for revised return filing",
    },
    
    "decriminalization": {
        "offences_decriminalized": 150,
        "compounding_enabled": True,
    },
}


def get_policy_by_sector(sector: str) -> dict:
    """Get all policies for a specific sector"""
    sector_map = {
        "infrastructure": INFRASTRUCTURE_POLICIES,
        "manufacturing": MANUFACTURING_POLICIES,
        "msme": MSME_POLICIES,
        "agriculture": AGRICULTURE_POLICIES,
        "employment": EMPLOYMENT_POLICIES,
        "health": HEALTH_POLICIES,
        "energy": ENERGY_POLICIES,
        "transport": TRANSPORT_TOURISM,
        "defence": DEFENCE_POLICIES,
        "digital": DIGITAL_POLICIES,
    }
    return sector_map.get(sector.lower(), {})


def get_total_allocation(sector: str) -> int:
    """Get total allocation for a sector in crores"""
    allocations = {
        "infrastructure": 1220000,
        "manufacturing": 159000,
        "msme": 12000,
        "agriculture": 14261,
        "employment": 29000,
        "health": 130000,
        "energy": 37700,
        "defence": 682000,
        "digital": 15372,
    }
    return allocations.get(sector.lower(), 0)