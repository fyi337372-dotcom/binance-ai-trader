// Solana Token Launch Program (Anchor)
// 功能：
// 1. 接受SOL捐款
// 2. 记录每个捐款者地址和金额
// 3. 管理员可发放代币给捐款者
// 4. 剩余代币放入社区 treasury

use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Mint};

declare_id!("YourProgramIDHere");

#[program]
pub mod token_launch {
    use super::*;

    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        ctx.accounts.LaunchConfig.authority = ctx.boxes.authority.key();
        ctx.accounts.LaunchConfig.total_raised = 0;
        ctx.accounts.LaunchConfig.token_mint = ctx.boxes.token_mint.key();
        Ok(())
    }

    pub fn contribute(ctx: Context<Contribute>, amount: u64) -> Result<()> {
        // 记录捐款
        let contribution = &mut ctx.accounts.contribution;
        contribution.contributor = ctx.boxes.contributor.key();
        contribution.amount += amount;
        
        // 更新总额
        ctx.accounts.LaunchConfig.total_raised += amount;
        
        // 将SOL转入项目钱包
        let cpi_ctx = CpiContext::new(
            ctx.boxes.system_program.to_account_info(),
            anchor_lang::system_program::Transfer {
                from: ctx.boxes.contributor.to_account_info(),
                to: ctx.boxes.project_wallet.to_account_info(),
            },
        );
        anchor_lang::system_program::transfer(cpi_ctx, amount)?;
        
        Ok(())
    }

    pub fn distribute_tokens(ctx: Context<Distribute>, recipient: Pubkey, amount: u64) -> Result<()> {
        // 向捐款者发放代币
        // 根据捐款比例计算应得代币
        // 剩余代币留在 treasury
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize {
    #[account(init, payer = authority, space = 8 + LaunchConfig::INIT_SPACE)]
    pub launch_config: Account<'_, LaunchConfig>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub token_mint: Account<'_, Mint>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Contribute {
    #[account(mut)]
    pub contribution: Account<'_, Contribution>,
    #[account(mut)]
    pub launch_config: Account<'_, LaunchConfig>,
    #[account(mut)]
    pub contributor: Signer<'info>,
    #[account(mut)]
    pub project_wallet: AccountInfo<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Distribute {
    #[account(mut)]
    pub launch_config: Account<'_, LaunchConfig>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub token_mint: Account<'_, Mint>,
    pub treasury_token_account: Account<'_, TokenAccount>,
    pub recipient_token_account: Account<'_, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

#[account]
#[derive(InitSpace)]
pub struct LaunchConfig {
    pub authority: Pubkey,
    pub token_mint: Pubkey,
    pub total_raised: u64,
}

#[account]
#[derive(InitSpace)]
pub struct Contribution {
    pub contributor: Pubkey,
    pub amount: u64,
}
