#!/usr/bin/env python3
"""Voronoi diagram — simplified computation via Delaunay dual."""
import math

def voronoi_edges(points):
    """Compute Voronoi edges as perpendicular bisectors between nearest neighbors."""
    n = len(points); edges = []
    for i in range(n):
        for j in range(i+1, n):
            mx = (points[i][0]+points[j][0])/2; my = (points[i][1]+points[j][1])/2
            dx = points[j][0]-points[i][0]; dy = points[j][1]-points[i][1]
            edges.append(((mx,my), (-dy, dx), i, j))  # midpoint, direction, sites
    return edges

def nearest_site(point, sites):
    best = 0; best_d = float('inf')
    for i, s in enumerate(sites):
        d = (point[0]-s[0])**2 + (point[1]-s[1])**2
        if d < best_d: best_d = d; best = i
    return best

def main():
    pts = [(0,0),(4,0),(2,3)]
    edges = voronoi_edges(pts)
    for mid, dir, i, j in edges:
        print(f"Edge between sites {i},{j}: midpoint={mid}, dir={dir}")

if __name__ == "__main__": main()
