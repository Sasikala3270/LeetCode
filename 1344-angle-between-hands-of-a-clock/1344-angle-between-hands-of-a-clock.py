class Solution(object):
    def angleClock(self, hour, minutes):
        h_angle = (hour % 12) * 30 + minutes * 0.5
        m_angle = minutes * 6
        angle = abs(h_angle - m_angle)
        return min(angle, 360 - angle)
        