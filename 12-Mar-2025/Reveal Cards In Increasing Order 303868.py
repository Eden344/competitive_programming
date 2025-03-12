# Problem: Reveal Cards In Increasing Order - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        que = deque(range(n))
        reveal= [0] * n
        deck.sort()

        for card in deck:
            reveal[que.popleft()] = card
            if que:
                que.append(que.popleft())
        return reveal


        


        