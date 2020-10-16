// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Framework/Commands/Commands.h"
#include "DoodleStyle.h"

class FDoodleCommands : public TCommands<FDoodleCommands>
{
public:

	FDoodleCommands()
		: TCommands<FDoodleCommands>(TEXT("Doodle"), NSLOCTEXT("Contexts", "Doodle", "Doodle Plugin"), NAME_None, FDoodleStyle::GetStyleSetName())
	{
	}

	// TCommands<> interface
	virtual void RegisterCommands() override;

public:
	TSharedPtr< FUICommandInfo > OpenPluginWindow;
};