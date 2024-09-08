# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 16:17:08 2024

@author: 91885
"""

from numpy import allclose 
## checking for the count of column numbers and if they are occuring consecutive.
def tables_are_consecutive(table1_info, table2_info):
    if table2_info['page'] == (table1_info['page'] + 1):
        if len(table2_info['cols']) == len(table1_info['cols']):

            # Extract the vertical coordinates of the tables
            _, y_bottom_table1, _, _ = table1_info['_bbox']
            _, _, _, y_top_table2 = table2_info['_bbox']

            page_height = 792

            # Check if the first table ends in the last 15% of the page
            # and the second table starts in the first 15% of the page
            if y_bottom_table1 < 0.15 * page_height and y_top_table2 > 0.85 * page_height:

                table1_column_widths = [col[1] - col[0] for col in table1_info['cols']]
                table2_column_widths = [col[1] - col[0] for col in table2_info['cols']]

                # Evaluate if the column widths of the two tables are similar
                return allclose(table1_column_widths, table2_column_widths, atol=3, rtol=0)

        return False
    return False
