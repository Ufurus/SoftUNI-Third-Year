from collections import deque

suggested_links = deque(list(map(int, input().split()))) # FIFO
featured_links = list(map(int, input().split())) # LIFO
target_engagement_value = int(input())
final_feed = []

while suggested_links and featured_links:

    current_suggested_link = suggested_links.popleft()
    current_featured_link = featured_links.pop()

    smaller_element = min([current_featured_link, current_suggested_link])
    greater_element = max([current_featured_link, current_suggested_link])

    if greater_element == smaller_element:
        final_feed.append(0)
        continue

    result = greater_element % smaller_element

    if greater_element == current_featured_link:
        final_feed.append(result)
        if result == 0:
            continue
        featured_links.append(result * 2)

    elif greater_element == current_suggested_link:
        final_feed.append(-result)
        if result == 0:
            continue
        suggested_links.append(result * 2)

print(f"Final Feed: {', '.join([str(x) for x in final_feed])}")
if sum(final_feed) >= target_engagement_value:
    print(f"Goal achieved! Engagement Value: {sum(final_feed)}")
else:
    print(f"Goal not achieved! Short by: {target_engagement_value - sum(final_feed)}")