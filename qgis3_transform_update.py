#Fixed shift coordinate system between indian1975 and wgs84
sources = []
sources.append(["EPSG:24047","EPSG:4326","+proj=pipeline +step +inv +proj=utm +zone=47 +ellps=evrst30 +step +proj=push +v_3 +step +proj=cart +ellps=evrst30 +step +proj=helmert +x=209 +y=818 +z=290 +step +inv +proj=cart +ellps=WGS84 +step +proj=pop +v_3 +step +proj=unitconvert +xy_in=rad +xy_out=deg"])
sources.append(["EPSG:24048","EPSG:4326","+proj=pipeline +step +inv +proj=utm +zone=48 +ellps=evrst30 +step +proj=push +v_3 +step +proj=cart +ellps=evrst30 +step +proj=helmert +x=209 +y=818 +z=290 +step +inv +proj=cart +ellps=WGS84 +step +proj=pop +v_3 +step +proj=unitconvert +xy_in=rad +xy_out=deg"])
sources.append(["EPSG:4326", "EPSG:24047","+proj=pipeline +step +proj=unitconvert +xy_in=deg +xy_out=rad +step +proj=push +v_3 +step +proj=cart +ellps=WGS84 +step +proj=helmert +x=-209 +y=-818 +z=-290 +step +inv +proj=cart +ellps=evrst30 +step +proj=pop +v_3 +step +proj=utm +zone=47 +ellps=evrst30"])
sources.append(["EPSG:4326", "EPSG:24048","+proj=pipeline +step +proj=unitconvert +xy_in=deg +xy_out=rad +step +proj=push +v_3 +step +proj=cart +ellps=WGS84 +step +proj=helmert +x=-209 +y=-818 +z=-290 +step +inv +proj=cart +ellps=evrst30 +step +proj=pop +v_3 +step +proj=utm +zone=48 +ellps=evrst30"])
sources.append(["EPSG:24047","EPSG:32647","+proj=pipeline +step +inv +proj=utm +zone=47 +ellps=evrst30 +step +proj=push +v_3 +step +proj=cart +ellps=evrst30 +step +proj=helmert +x=209 +y=818 +z=290 +step +inv +proj=cart +ellps=WGS84 +step +proj=pop +v_3 +step +proj=utm +zone=47 +ellps=WGS84"])
sources.append(["EPSG:24048","EPSG:32648","+proj=pipeline +step +inv +proj=utm +zone=47 +ellps=evrst30 +step +proj=push +v_3 +step +proj=cart +ellps=evrst30 +step +proj=helmert +x=209 +y=818 +z=290 +step +inv +proj=cart +ellps=WGS84 +step +proj=pop +v_3 +step +proj=utm +zone=48 +ellps=WGS84"])
sources.append(["EPSG:24047","EPSG:32648","+proj=pipeline +step +inv +proj=utm +zone=47 +ellps=evrst30 +step +proj=push +v_3 +step +proj=cart +ellps=evrst30 +step +proj=helmert +x=209 +y=818 +z=290 +step +inv +proj=cart +ellps=WGS84 +step +proj=pop +v_3 +step +proj=utm +zone=47 +ellps=WGS84"])
sources.append(["EPSG:24048","EPSG:32647","+proj=pipeline +step +inv +proj=utm +zone=47 +ellps=evrst30 +step +proj=push +v_3 +step +proj=cart +ellps=evrst30 +step +proj=helmert +x=209 +y=818 +z=290 +step +inv +proj=cart +ellps=WGS84 +step +proj=pop +v_3 +step +proj=utm +zone=48 +ellps=WGS84"])
sources.append(["EPSG:32647","EPSG:24047","+proj=pipeline +step +inv +proj=utm +zone=47 +ellps=WGS84 +step +proj=push +v_3 +step +proj=cart +ellps=WGS84 +step +proj=helmert +x=-209 +y=-818 +z=-290 +step +inv +proj=cart +ellps=evrst30 +step +proj=pop +v_3 +step +proj=utm +zone=47 +ellps=evrst30"])
sources.append(["EPSG:32648","EPSG:24048","+proj=pipeline +step +inv +proj=utm +zone=47 +ellps=WGS84 +step +proj=push +v_3 +step +proj=cart +ellps=WGS84 +step +proj=helmert +x=-209 +y=-818 +z=-290 +step +inv +proj=cart +ellps=evrst30 +step +proj=pop +v_3 +step +proj=utm +zone=48 +ellps=evrst30"])
sources.append(["EPSG:32647","EPSG:24048","+proj=pipeline +step +inv +proj=utm +zone=47 +ellps=WGS84 +step +proj=push +v_3 +step +proj=cart +ellps=WGS84 +step +proj=helmert +x=-209 +y=-818 +z=-290 +step +inv +proj=cart +ellps=evrst30 +step +proj=pop +v_3 +step +proj=utm +zone=47 +ellps=evrst30"])
sources.append(["EPSG:32648","EPSG:24047","+proj=pipeline +step +inv +proj=utm +zone=47 +ellps=WGS84 +step +proj=push +v_3 +step +proj=cart +ellps=WGS84 +step +proj=helmert +x=-209 +y=-818 +z=-290 +step +inv +proj=cart +ellps=evrst30 +step +proj=pop +v_3 +step +proj=utm +zone=48 +ellps=evrst30"])
sources.append(["EPSG:24047","EPSG:3857","+proj=pipeline +step +inv +proj=utm +zone=47 +ellps=evrst30 +step +proj=push +v_3 +step +proj=cart +ellps=evrst30 +step +proj=helmert +x=209 +y=818 +z=290 +step +inv +proj=cart +ellps=WGS84 +step +proj=pop +v_3 +step +proj=webmerc +lat_0=0 +lon_0=0 +x_0=0 +y_0=0 +ellps=WGS84"])
sources.append(["EPSG:24048","EPSG:3857","+proj=pipeline +step +inv +proj=utm +zone=48 +ellps=evrst30 +step +proj=push +v_3 +step +proj=cart +ellps=evrst30 +step +proj=helmert +x=209 +y=818 +z=290 +step +inv +proj=cart +ellps=WGS84 +step +proj=pop +v_3 +step +proj=webmerc +lat_0=0 +lon_0=0 +x_0=0 +y_0=0 +ellps=WGS84"])
sources.append(["EPSG:3857","EPSG:24047","+proj=pipeline +step +inv +proj=webmerc +lat_0=0 +lon_0=0 +x_0=0 +y_0=0 +ellps=WGS84 +step +proj=push +v_3 +step +proj=cart +ellps=WGS84 +step +proj=helmert +x=-209 +y=-818 +z=-290 +step +inv +proj=cart +ellps=evrst30 +step +proj=pop +v_3 +step +proj=utm +zone=47 +ellps=evrst30"])
sources.append(["EPSG:3857","EPSG:24048","+proj=pipeline +step +inv +proj=webmerc +lat_0=0 +lon_0=0 +x_0=0 +y_0=0 +ellps=WGS84 +step +proj=push +v_3 +step +proj=cart +ellps=WGS84 +step +proj=helmert +x=-209 +y=-818 +z=-290 +step +inv +proj=cart +ellps=evrst30 +step +proj=pop +v_3 +step +proj=utm +zone=48 +ellps=evrst30"])

for source in sources:
	parent = source[0]
	sibling = source[1] + '_coordinateOp'
	option = source[2]
	fallback= parent + '_allowFallback'
	sfall = source[1] + '_allowFallback'
	QSettings().setValue("projections/%s/%s" % (parent,sibling), option)
	QSettings().setValue("projections/%s/%s" % (parent,fallback), True)
	QSettings().setValue("projections/%s/%s" % (parent,sfall), True)

iface.reloadConnections()
print('update success!!!')