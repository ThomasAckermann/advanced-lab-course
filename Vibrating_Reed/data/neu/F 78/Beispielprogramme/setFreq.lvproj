<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="10008000">
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="setFreq.vi" Type="VI" URL="../setFreq.vi"/>
		<Item Name="Dependencies" Type="Dependencies"/>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="setFreq" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{35D4DD59-5E8E-11E8-A3A3-001E0BA6D521}</Property>
				<Property Name="App_INI_GUID" Type="Str">{35D4DA43-5E8E-11E8-A3A3-001E0BA6D521}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">setFreq</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/setFreq/setFreq</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Destination[0].destName" Type="Str">Application</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/NI_AB_PROJECTNAME/setFreq/Application</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/NI_AB_PROJECTNAME/setFreq/data</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{1F935D4F-5E8E-11E8-8513-001E0BA6D521}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/setFreq.vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="TgtF_fileDescription" Type="Str">setFreq</Property>
				<Property Name="TgtF_fileVersion.major" Type="Int">1</Property>
				<Property Name="TgtF_internalName" Type="Str">setFreq</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright 2018 </Property>
				<Property Name="TgtF_productName" Type="Str">setFreq</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{35D508D3-5E8E-11E8-A3A3-001E0BA6D521}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">Application</Property>
			</Item>
		</Item>
	</Item>
</Project>
