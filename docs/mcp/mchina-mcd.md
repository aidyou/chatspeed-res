---
title: "mcd_mcp_server"
description: "Introduction What is McDonald's MCP Service? - McDonald's MCP Service is a data interaction interface service that adheres to the Model Context Protocol (MCP) standard, provided by McDonald's China fo…"
---

# mcd_mcp_server

Introduction What is McDonald's MCP Service? - McDonald's MCP Service is a data interaction interface service that adheres to the Model Context Protocol (MCP) standard, provided by McDonald's China fo…

# Introduction

**What is McDonald's MCP Service?**
- McDonald's MCP Service is a data interaction interface service that adheres to the Model Context Protocol (MCP) standard, provided by McDonald's China for use in mainland China (excluding Hong Kong, Macau, and Taiwan).
- The McDonald's MCP Service now covers business scenarios such as McDelivery ordering, points redemption coupons, and event calendar queries. More practical tools are continuously being developed and launched.

# News
- **[2026-02] `Feature`:** We have added the "McDelivery Ordering" and "Points Redemption Coupons" feature modules, supporting complete delivery ordering and points redemption services. [View Tool Details](#4-Tools)
- **[2026-01] `Feature`:** We have added the "Nutrition Information List of Meals" tool, allowing users to query nutritional data for common McDonald's meals, including calories and nutrition. [View Tool Details](#4-Tools)
- **[2025-12] `Release`:** We released McDonald's MCP Server version 1.0.0, providing event calendar queries and coupon redemption features. Give it a try! For integration tutorials, see the [Quick Start](#2-Quick-Start) section below.

# How to Use McDonald's MCP Service on ModelScope?
We have already deployed the McDonald's MCP Service in the cloud for you. You need to go to the [McDonald's MCP Platform](https://open.mcd.cn/mcp), log in, and obtain an MCP Token. The MCP Service currently supports adding to agents and workflows.

For detailed instructions on obtaining an MCP Token, see the [McDonald's MCP Platform](https://open.mcd.cn/mcp).

# List of Tools in McDonald's MCP Service

  

    

      

Tool

      

Name

      

Description

    

  

  

    

      
list-nutrition-foods

      
Nutrition Information List of Meals

      
Obtain nutritional data for common McDonald's meals, including energy, protein, fat, carbohydrates, sodium, calcium, etc. This is useful when users inquire about the calories and nutrition of McDonald's meals and need to pair them with specific calorie meal sets.

    

    

      
delivery-query-addresses

      
Get User's Deliverable Address List

      
Query the list of delivery addresses created by the user, used for selecting a delivery address during McDelivery ordering and obtaining corresponding store information (storeCode, beCode).

    

    

      
delivery-create-address

      
Add Delivery Address

      
Used when the user has no deliverable address or needs to add a new delivery address, for creating a new deliverable address.

    

    

      
query-usable-coupons

      
Query Usable Coupons at Current Store

      
Query the list of usable coupons for the user at the current store, used for selecting available discounts during ordering.

    

    

      
query-meals

      
Query List of Sellable Meals at Current Store

      
Query the menu of sellable meals at the current store (categories, meal codes, tags, etc.), used for meal selection during ordering.

    

    

      
meal-detail

      
Query Meal Details

      
Query meal details based on the meal code (meal composition, default selections, etc.), used for viewing the contents of a meal set.

    

    

      
calculate-price

      
Calculate Product Price

      
Calculate the total amount, delivery fee, discount amount, and payable total based on the user's selected product list (which may include coupons).

    

    

      
create-order

      
Create Delivery Order

      
Create a delivery order based on store information, delivery address, and product list, returning order details and payment link.

    

    

      
query-order

      
Query Order Details

    

  

Query order status, order details, delivery information, etc., for users to check order progress or confirm order information

    

    

      
campaign-calendar

      
Campaign calendar query tool

      
Query McDonald's China's marketing campaign calendar for the current month, returning ongoing, past, and future events

    

    

      
available-coupons

      
McSavings coupon list query

      
Query the list of McSavings coupons that the user can currently claim

    

    

      
auto-bind-coupons

      
One-click McSavings coupon claiming

      
Automatically claim all currently available McDonald's coupons from McSavings. No need to specify individual coupons or coupon IDs; the system will automatically claim all eligible coupons for the user

    

    

      
my-coupons

      
My coupons query

      
Query which coupons are available for use. Similar to opening the "My Coupons" page in the McDonald's App, where you can see a list of all coupons that can be used for ordering

    

    

      
query-my-account

      
My points query

      
Query the user's points account information, including available points, accumulated points, frozen points, and points about to expire

    

    

      
mall-points-products

      
Points redeemable product list

      
Query the list of meal vouchers that can be redeemed with points in the McSavings Mall (excluding physical items or third-party codes redeemable with points)

    

    

      
mall-product-detail

      
Points redeemable product detail

      
Query detailed information about a specific points-redeemable meal voucher (images, points required, validity period, description, details, etc.)

    

    

      
mall-create-order

      
Points redeemable product order creation

      
Use points to redeem a specific meal voucher, complete the points deduction, and issue the voucher code, returning the redemption order number and voucher code information

    

    

      
now-time-info

      
Get current time information

      
Return the full current time information so that the LLM knows the current time and date

    

  

# Frequently Asked Questions
Q: Is there a charge for using McDonald's MCP services?\
A: No, it is free.

# Version Log

|    Date    | Version | Description                        |
|:----------:|:-------:|------------------------------------|
| 2025-12-09 |  1.0.0  | McCalendar and McSavings Coupon MCP Server              |
| 2026-01-23 |  1.0.1  | Added "Nutritional Information List" Tool, shortened URL for easier access |
| 2026-02-13 |  1.0.2  | Added Tools for McDelivery ordering and points redemption scenarios             |

---

# Notes
1. Individuals are allowed to copy and use the example configurations, parameters, JSON, or sample code in the McDonald's MCP platform documentation for non-commercial purposes, solely for connecting and using the McDonald's MCP services.
2. Use of the McDonald's MCP service must comply with McDonald's China's "Terms of Use" and "McDonald's MCP Service Rules," and you must agree to these terms when applying for an MCP Token.
3. Without written authorization, the content of this document may not be used for commercial sales, paid distribution, traffic monetization, or any purpose that implies official endorsement or misleads the public; nor may it be used for any illegal, non-compliant, or black/gray market activities.
4. The content of this document is provided "as is" and does not constitute any form of warranty or commitment.
5. This document does not constitute any authorization for the trademarks of McDonald's and its affiliates.
6. Please keep your MCP Token secure to prevent leakage or unauthorized use.

© 2026 McDonald’s. All Rights Reserved.

**Official site: ** [https://open.mcd.cn/mcp](https://open.mcd.cn/mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`, `data`
- Tags: `other`, `calendar management`, `location services`, `麦当劳`, `美食`, `餐饮`, `生活服务`, `chinese`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/mchina-mcd.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
