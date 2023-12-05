SCREEN_SIZE = 120
TOTAL_COMPONENTS = 4
BLOCK_WIDTH=SCREEN_SIZE // TOTAL_COMPONENTS

#initialize array
COMPONENT_ARRAY = []

#method for components
def create_componets():
    for i in range(TOTAL_COMPONENTS):
        component_start = i * BLOCK_WIDTH
        component_end = (i+1) * BLOCK_WIDTH - 1
        COMPONENT_ARRAY.append((component_start,component_end))

create_componets()
#components
print("components :")

#print components

for components in COMPONENT_ARRAY:
    print(f"first : {components[0]}, end :{components[1]}")